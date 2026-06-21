# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05279():
    auth_header = request.headers.get('Authorization', '')
    data = default_blank(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
