# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import request, jsonify
import json
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest01282():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
