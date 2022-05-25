import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


import acquire

########## TELCO DATA ###########
def clean_telco_data(df):
    '''This function cleans the data from the original dataset by dropping nulls and unnnecesary
    columns, changes columns to the data type that makes sense (ie. total_charges to float), and
    coverts categorical columns with one-hot encoding to allow for input into models.
    '''
    # replace empty cells with nulls
    df = df.replace(' ', np.nan)
    # drop 11 nulls from total_charges
    df.dropna(inplace=True)
    # change total_charges to float
    df['total_charges'] = pd.to_numeric(df['total_charges'])
    # drop unnecessary columns
    df = df.drop(columns=['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    # convert categorical columns to boolean
    df['is_female'] = df['gender'].map({'Female': 1, 'Male': 0})
    df['has_partner'] = df['partner'].map({'Yes': 1, 'No': 0})
    df['has_dependents'] = df['dependents'].map({'Yes': 1, 'No': 0})
    df['has_phone_service'] = df['phone_service'].map({'Yes': 1, 'No': 0})
    df['has_paperless_billing'] = df['paperless_billing'].map({'Yes': 1, 'No': 0})
    df['has_churned'] = df['churn'].map({'Yes': 1, 'No': 0})
    
    # encode categorical columns 
    dummy_df = pd.get_dummies(df[['contract_type','internet_service_type', 'payment_type',\
                              'multiple_lines', 'online_security', 'online_backup',\
                              'tech_support', 'streaming_tv', 'streaming_movies']],dummy_na=False, drop_first=True)
    #combine dataframes
    df = pd.concat([df, dummy_df], axis=1)
    
    return df


def split_telco_data(df):
    ''' This function splits the cleaned dataframe into train, validate, and test 
    datasets and statrifies based on the target, churn.'''

    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    
    return train, validate, test
    

    