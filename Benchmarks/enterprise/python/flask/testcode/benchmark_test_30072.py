# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30072():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
