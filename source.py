import pandas as pd
import os

# delete files if exist
if os.path.exists('csv/Fact_Source.csv'):
    os.remove('csv/Fact_Source.csv')

# Read data
participants=pd.read_csv('csv/Dim_Participant.csv')
source=pd.read_csv('csv/Dim_Source.csv')
# Merge data
sales=pd.merge(participants,source,on=['id'],how='inner')

# create new file named fact_sales.csv
sales.to_csv('csv/Fact_Source.csv',index=False)