# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest26156():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
