# SPDX-License-Identifier: Apache-2.0
import requests
from dataclasses import dataclass
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


@dataclass
class FormData:
    payload: str

def BenchmarkTest07741():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
