# -*- coding: utf-8
import os, re, subprocess
import ConfigParser
from tempfile import NamedTemporaryFile

CONFIG_FILE = 'config.ini'

def notice(msg, title="notice"): 
    ''' notoce message in notification center'''
    os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))

def read_config():
    ''' read congig from config.ini, return a five tuple'''
    if not os.path.exists(CONFIG_FILE):
        return
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    s3_section = 's3'
    keys = ('ak', 'sk', 'endpoint', 'bucket', 'signerVersion', 'prefix')
    try:
        res = map(lambda x: cf.get(s3_section, x), keys)
    except ConfigParser.NoOptionError:
        return

    if not all(map(lambda x: re.match(r'\w+', x), res)):
        return
    return dict(zip(keys, res))

def open_with_editor(filepath):
    ''' open file with apple's text editor'''
    os.system('open -b "com.apple.TextEdit" "./%s"' % CONFIG_FILE)

def generate_config_file():
    import textwrap
    config_file_init_content = '''\
    ; 详细设置见 https://github.com/tiann/markdown-img-upload
    [qiniu]
    ak=Access Key
    sk=Secret Key
    endpoint=endpoint
    bucket=bucket
    signerVersion=signerVersion'''
    with open(CONFIG_FILE, 'w') as fp:
        fp.write(textwrap.dedent(config_file_init_content))

def try_compress_png(raw_img, need_compress):
    ''' use pngquant to compress:https://github.com/pornel/pngquant'''
    if not need_compress: return raw_img
    if not os.path.exists(raw_img.name): return raw_img
    tmp_file = NamedTemporaryFile()
    return tmp_file if not subprocess.call('pngquant/pngquant --force %s -o %s' \
        % (raw_img.name, tmp_file.name), shell=True) else raw_img
