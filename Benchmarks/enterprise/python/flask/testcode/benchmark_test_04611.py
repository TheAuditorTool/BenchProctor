# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest04611():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    int(str(data))
    return jsonify({"result": "success"})
