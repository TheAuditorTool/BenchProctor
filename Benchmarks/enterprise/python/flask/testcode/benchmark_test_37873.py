# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest37873():
    raw_body = request.get_data(as_text=True)
    data = coalesce_blank(raw_body)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
