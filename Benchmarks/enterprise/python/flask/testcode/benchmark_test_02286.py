# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest02286():
    raw_body = request.get_data(as_text=True)
    _resp = requests.get(str(raw_body))
    exec(_resp.text)
    return jsonify({"result": "success"})
