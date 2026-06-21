# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest52936():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    json.loads(data)
    return jsonify({"result": "success"})
