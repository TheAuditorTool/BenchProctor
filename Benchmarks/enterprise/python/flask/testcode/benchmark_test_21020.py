# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest21020():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
