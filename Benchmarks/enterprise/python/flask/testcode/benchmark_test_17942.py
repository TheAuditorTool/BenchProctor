# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os


def BenchmarkTest17942():
    user_id = request.args.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return jsonify({"result": "success"})
