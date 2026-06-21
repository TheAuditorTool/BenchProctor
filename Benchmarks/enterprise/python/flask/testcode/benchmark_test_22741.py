# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest22741():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
