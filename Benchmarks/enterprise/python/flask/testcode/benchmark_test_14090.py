# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
from app_runtime import db


def BenchmarkTest14090():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
