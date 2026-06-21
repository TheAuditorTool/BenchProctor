# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


@dataclass
class FormData:
    payload: str

def BenchmarkTest18973():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
