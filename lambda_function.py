# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import boto3
import pandas as pd
def lambda_handler():
    bucket_name = 'ss-data-validation'
    s3_path = "test/"
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket=bucket_name, Key=s3_path+'EMT Shipowners Exposure 07-06-2021 (2).xlsx')
    print(data['Body'])
    read_file = pd.read_excel(data, header=1)
    print(read_file)
    s3.Bucket(bucket_name).put_object(Key=s3_path)
    read_file.to_csv("ss-data-validation/test", index=None, encoding="UTF-8")


if __name__ == "__main__":
    lambda_handler()
