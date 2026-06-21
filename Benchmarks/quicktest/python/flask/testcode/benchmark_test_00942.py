# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00942():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
