# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest53404():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    eval(compile("_resp = requests.get(str(data))\ndb.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
