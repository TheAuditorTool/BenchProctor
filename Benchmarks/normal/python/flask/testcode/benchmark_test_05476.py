# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest05476():
    auth_header = request.headers.get('Authorization', '')
    data = relay_value(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
