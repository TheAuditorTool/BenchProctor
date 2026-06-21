# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest78130():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
