import pandas as pd
import numpy as np
import os
from env import get_db_url
    
    



def get_telco_data():

    '''This function pulls telco data from the Codeup database and saves
    the file as a .csv'''
    filename = 'telco_data.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
       sql_query = '''SELECT * from customers
                JOIN contract_types using (contract_type_id)
                JOIN internet_service_types using (internet_service_type_id)
                JOIN payment_types using (payment_type_id)'''
       
    
    df = pd.read_sql(sql_query, get_db_url('telco_churn'))

    df.to_csv(filename)

    return df