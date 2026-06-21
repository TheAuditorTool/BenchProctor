# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import os


def BenchmarkTest53385():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})
