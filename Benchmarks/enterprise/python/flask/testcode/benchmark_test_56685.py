# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os


def BenchmarkTest56685():
    raw_body = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
