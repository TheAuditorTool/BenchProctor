# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest12357():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    if time.time() > 1000000000:
        return render_template_string(data)
    return jsonify({"result": "success"})
