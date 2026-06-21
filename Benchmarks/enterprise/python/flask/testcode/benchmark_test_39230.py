# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest39230():
    env_value = os.environ.get('USER_INPUT', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(env_value)), context=ctx)
    return jsonify({"result": "success"})
