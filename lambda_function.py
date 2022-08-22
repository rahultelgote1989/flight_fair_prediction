import json
import boto3
import pandas

IP_BUCKET_NAME = 'user-tweets-input'
OP_BUCKET_NAME = 'user-sentiments-output'


s3_conn = boto3.client("s3")

all_files = []

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    s3_client = boto3.client("s3")
    comprehend_client = boto3.client("comprehend")
    my_bucket = s3.Bucket(IP_BUCKET_NAME)
    for object_summary in my_bucket.objects.filter():
        _file_name = object_summary.key
        _file_text = s3_client.get_object(Bucket=IP_BUCKET_NAME, Key=_file_name)
        data = _file_text["Body"].read()
        df = pandas.read_excel(data, header=1)
        print(df.head(10))
        return
        # for batch in data[::5000]
        # sent_data = comprehend_client.detect_sentiment(Text=data[:4500], LanguageCode="en")
        # return sent_data
        
        
