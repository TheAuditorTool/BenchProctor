# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest50886():
    upload_name = request.files['upload'].filename
    data = normalise_input(upload_name)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
