# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest66804():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
