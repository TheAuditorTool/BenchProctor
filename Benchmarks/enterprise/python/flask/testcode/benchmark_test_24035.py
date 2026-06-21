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

def BenchmarkTest24035():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
