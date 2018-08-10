# -*- coding: utf-8 -*-
from mssapi.s3.connection import S3Connection
from util import read_config

config = read_config()


def s3conn():
    conn = S3Connection(
        aws_access_key_id=config['ak'],
        aws_secret_access_key=config['sk'],
        is_secure = False,
        host=config['endpoint'])
    return conn

bs = s3conn().get_all_buckets()
for b in bs:
    print b.name

def upload_local_file(path, upload_name):
    bucket = s3conn().get_bucket(config['bucket'])
    k0 = bucket.new_key(upload_name)
    size = k0.set_contents_from_filename(path,replace=True)
    return size

if __name__ == '__main__':
    upload_local_file('/Users/yeanzhi/Pictures/3fc03788d2b845ff36b5ded0dc502270.jpg','3fc03788d2b845ff36b5ded0dc502270.jpg')
