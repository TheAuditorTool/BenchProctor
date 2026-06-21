# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


@dataclass
class FormData:
    payload: str

def BenchmarkTest10603():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
