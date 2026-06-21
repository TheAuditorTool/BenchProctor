# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os
from flask import jsonify


def BenchmarkTest28126():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})
