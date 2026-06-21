# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def BenchmarkTest76985():
    raw_body = request.get_data(as_text=True)
    requests.get(str(raw_body))
    return jsonify({"result": "success"})
