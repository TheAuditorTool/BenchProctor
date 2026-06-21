# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest12487():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    requests.get(str(data))
    return jsonify({"result": "success"})
