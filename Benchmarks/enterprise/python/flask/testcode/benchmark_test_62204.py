# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
from app_runtime import db


def BenchmarkTest62204():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
