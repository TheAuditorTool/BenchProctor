# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request
import urllib.parse
import ssl


request_state: dict[str, str] = {}

def BenchmarkTest25392():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
