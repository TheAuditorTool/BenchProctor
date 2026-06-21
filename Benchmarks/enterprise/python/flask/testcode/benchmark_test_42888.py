# SPDX-License-Identifier: Apache-2.0
import requests
import base64
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest42888():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
