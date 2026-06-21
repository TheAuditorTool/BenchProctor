# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request, jsonify
import os


def BenchmarkTest76969():
    raw_body = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return jsonify({"result": "success"})
