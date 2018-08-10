# -*- coding: utf-8 -*-
from mssapi.s3.connection import S3Connection
from util import read_config

config = read_config()
conn = S3Connection(
    aws_access_key_id=config['ak'],
    aws_secret_access_key=config['sk'],
    is_secure = False,
    host=config['endpoint'])

b0 = conn.get_bucket(config['bucket'])

def upload_file(path, upload_name):
    k0 = b0.new_key(upload_name)
    return k0.set_contents_from_filename(path)
