# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os


def BenchmarkTest25664():
    auth_header = request.headers.get('Authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return jsonify({"result": "success"})
