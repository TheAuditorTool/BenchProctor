# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest26958():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
