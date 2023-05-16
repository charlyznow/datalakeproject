import configparser
import boto3

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

access_key = config.get('s3', 'access_key')
secret_key = config.get('s3', 'secret_key')

source_path = config.get('settings', 'source_path')
target_path = config.get('settings' , 'target_path')


my_bucket= 'cheems-datalake'
file= f'{source_path}/logo.jpg'

s3_client = boto3.client('s3')

def list_data():
    try:
        response = s3_client.list_objects(Bucket=my_bucket)
        if 'Contents' in response:
            print('Have This files into the Bucket: ')
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print('No Files Into the Bucket')
    except s3_client.exceptions.NoSuchBucket:
        print(f'El Bucket {my_bucket} no existe')

def  download_data(file,bucket_path):
    try:
        s3_client.download_file(source_path ,file, target_path)
        print(f'File {file} Download Correctly')
    except s3_client.exceptions.ClientError as e:
        print(f'Error to Download File: {e}')


#list_data()
download_data(file, target_path)

