import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


import acquire

########## TELCO DATA ###########
def prep_telco(df):
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    df['total_charges'] = df.total_charges.astype(float)
    columns_to_drop = ['Unnamed: 0','internet_service_type_id', 'payment_type_id', 'contract_type_id']
    df = df.drop(columns = columns_to_drop)
    df['is_female'] = df['gender'].map({'Female': 1, 'Male': 0})
    df['has_partner'] = df['partner'].map({'Yes': 1, 'No': 0})
    df['has_dependents'] = df['dependents'].map({'Yes': 1, 'No': 0})
    df['has_phone_service'] = df['phone_service'].map({'Yes': 1, 'No': 0})
    df['has_paperless_billing'] = df['paperless_billing'].map({'Yes': 1, 'No': 0})
    df['has_churned'] = df['churn'].map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(df[['gender', 'partner', 'phone_service', \
                                  'multiple_lines', 'online_security', \
                                  'online_backup', 'tech_support', \
                                  'streaming_tv', 'streaming_movies', \
                                  'paperless_billing', 'churn', 'contract_type', \
                                  'internet_service_type', 'payment_type']], \
                              dummy_na=False, drop_first=False)
    df = pd.concat([df, dummy_df], axis=1)
    return df

    