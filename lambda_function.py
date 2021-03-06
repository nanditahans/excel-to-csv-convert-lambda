# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import sys

def lambda_handler(event, context):
    try:
        bucket_name = 'ss-data-validation'
        xlsx = ".xlsx"
        csv = ".csv"
        s3_path = event['s3-path']
        file_name = event['file_name']
        fileType = event['fileType']
        print(s3_path)
        print(file_name)
        data_file_url = "s3://" + bucket_name + "/" + s3_path + file_name + xlsx
        print(data_file_url)
        if fileType == "claims":
            print(fileType)
            read_file = pd.read_excel(data_file_url, engine='openpyxl', sheet_name=1)
            read_file.dropna(how="all", inplace=True)
            read_file.rename(columns={'Claim ID': 'Claim_ID'}, inplace=True)
            read_file['IMO'] = read_file['IMO'].astype(int)
        else:
            print(fileType)
            read_file = pd.read_excel(data_file_url, header=1, engine='openpyxl')
            read_file.dropna(how="all", inplace=True)
        read_file.to_csv("s3://" + bucket_name + "/" + s3_path + file_name + csv, index=None, encoding="UTF-8")
        return file_name+csv
    except:
        print("Oops!", sys.exc_info(), "occurred.")
