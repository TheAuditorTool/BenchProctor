# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest17690():
    origin_value = request.headers.get('Origin', '')
    data = to_text(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
