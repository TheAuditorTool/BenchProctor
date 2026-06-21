# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import time


def relay_value(value):
    return value

def BenchmarkTest23560():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    if time.time() > 1000000000:
        return render_template_string(data)
    return jsonify({"result": "success"})
