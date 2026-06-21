# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import request, jsonify
import os
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest15242():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    _cipher = Fernet(os.environ['DATA_ENC_KEY'].encode())
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
