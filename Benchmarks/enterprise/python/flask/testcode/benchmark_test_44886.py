# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest44886():
    upload_name = request.files['upload'].filename
    data = normalise_input(upload_name)
    int(str(data))
    return jsonify({"result": "success"})
