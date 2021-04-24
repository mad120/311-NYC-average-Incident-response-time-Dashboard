# 311-NYC-average-Incident-response-time-Dashboard
The Dataset can be found here: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9  
Once Downloaded, run the bash file trimmed.sh The output (new3.csv) will be the incidents occured in 2020 only.  
Then run the task_2_data_cleaning.ipynb file which will perform data cleaning and output the final cleaned version as "FINAL_small_closed_incident_drop_na_time_diff__positive_month.csv"
Finally run the main.py and execute the following command in the terminal:  
bokeh serve --show nyc_dash --port 8080
