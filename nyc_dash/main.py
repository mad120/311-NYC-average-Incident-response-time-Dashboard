#!/usr/bin/env python
# coding: utf-8
from bokeh.plotting import figure, curdoc, output_file, show
from bokeh.layouts import column
from bokeh.models import Button, Select, ColumnDataSource
from bokeh.io import curdoc
import pandas as pd
import numpy as np


df = pd.read_csv("FINAL_small_closed_incident_drop_na_time_diff__positive_month.csv", low_memory=False)
unique_zip_array=df["Zip"].dropna().unique()

months_dict_all={
    "1":None,
    "2":None,
    "3":None,
    "4":None,
    "5":None,
    "6":None,
    "7":None,
    "8":None,
    "9":None,    
}

for i in months_dict_all:
    months_dict_all[i]=df[df["Month_number"] == int(i)]['time_diff_in_hour'].mean()

months_dict_zipcode={
    "1":None,
    "2":None,
    "3":None,
    "4":None,
    "5":None,
    "6":None,
    "7":None,
    "8":None,
    "9":None,
}

def select_zipcode(zip_value):

    for i in months_dict_zipcode:
        months_dict_zipcode[i]=df[(df["Month_number"] == int(i)) & (df["Zip"]==zip_value)]['time_diff_in_hour'].mean()

        
zip_array = np.unique(df["Zip"])
#zip_array = np.delete(zip_array, 0)
zip_str = zip_array.astype(int).astype(str)
zip_list = zip_str.tolist()

all_zipcode_and_values = {}

for zipcode in zip_list:
    select_zipcode(float(zipcode))
    all_zipcode_and_values[zipcode] = months_dict_zipcode.copy()


default_zip1 = '10000'
default_zip2 = '10001'
list(months_dict_all.keys())
x1=list(months_dict_all.keys())
x2=list(all_zipcode_and_values[default_zip1].keys())
x3=list(all_zipcode_and_values[default_zip2].keys())

y1=list(months_dict_all.values())
y2=list(all_zipcode_and_values[default_zip1].values())
y3=list(all_zipcode_and_values[default_zip2].values())

source1 = ColumnDataSource(data=dict(x=x1, y=y1))
source2 = ColumnDataSource(data=dict(x=x2, y=y2))
source3 = ColumnDataSource(data=dict(x=x3, y=y3))

p = figure(
    title='NYC Bokeh Dashboard',
    x_axis_label='Months (in digit)',
    y_axis_label='Average Response Time (in hour)'
    )

p.line('x', 'y', source=source1, line_alpha=0.6, color="red", line_width=3, legend_label="All Data")
p.line('x', 'y', source=source2, line_alpha=0.6, color="blue", line_width=3, legend_label="Zipcode 1")
p.line('x', 'y', source=source3, line_alpha=0.6, color="green", line_width=3, legend_label="Zipcode 2")

#Styling legend
p.legend.location = 'top_left'
p.legend.title_text_font_size = '12pt'

select1= Select(title="Zipcode 1", value=default_zip1, options = zip_list)
select2= Select(title="Zipcode 2", value=default_zip2, options = zip_list)


def update_data(attrname, old, new):
    z1 = select1.value
    z2 = select2.value
    
    x1=list(months_dict_all.keys())
    x2=list(all_zipcode_and_values[z1].keys())
    x3=list(all_zipcode_and_values[z2].keys())

    y1=list(months_dict_all.values())
    y2=list(all_zipcode_and_values[z1].values())
    y3=list(all_zipcode_and_values[z2].values())

    source1.data = dict(x=x1, y=y1)
    source2.data = dict(x=x2, y=y2)
    source3.data = dict(x=x3, y=y3)


for w in [select1, select2]:
    w.on_change('value', update_data)

    
curdoc().add_root(column(select1,select2, p))
curdoc().title = "nyc_dash"