# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest36912():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
