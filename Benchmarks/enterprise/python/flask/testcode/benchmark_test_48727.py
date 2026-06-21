# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest48727():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
