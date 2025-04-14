#!/bin/bash

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <file> <bucket> <expires_in>"
  exit 1
fi

file=$1
bucket=$2
expi=$3

[ ! -f "$f" ] && echo "File not found" && exit 2

aws s3 cp "$f" "s3://$b/" || exit 3

url=$(aws s3 presign "s3://$b/$(basename "$f")" --expires-in "$e") || exit 4

echo "$url"

