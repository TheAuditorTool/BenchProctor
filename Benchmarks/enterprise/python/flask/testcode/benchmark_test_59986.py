# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest59986():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
