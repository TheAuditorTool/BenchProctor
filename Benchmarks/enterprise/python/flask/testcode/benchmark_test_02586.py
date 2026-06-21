# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest02586():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
