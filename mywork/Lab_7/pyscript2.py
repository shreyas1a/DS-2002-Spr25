#!/usr/bin/env python3
import requests, boto3, sys

url = "https://flickr.com/albums/photos/no-composure-c-4_54446364164_o.jpg"
filename = "no-composure-band-pic.jpg"
bucket = "bucketnumberone"
expires = 604800

r = requests.get(url)
if r.status_code != 200:
    print("Failed to download")
    sys.exit(1)

with open(filename, "wb") as f:
    f.write(r.content)

s3 = boto3.client("s3", region_name="us-east-1")
s3.upload_file(filename, bucket, filename, ExtraArgs={'ACL': 'private'})

url = s3.generate_presigned_url("get_object", Params={"Bucket": bucket, "Key": filename}, ExpiresIn=expires)
print(url)
