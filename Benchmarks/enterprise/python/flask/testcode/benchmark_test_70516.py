# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest70516():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
