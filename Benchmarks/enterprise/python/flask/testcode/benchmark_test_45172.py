# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest45172():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
