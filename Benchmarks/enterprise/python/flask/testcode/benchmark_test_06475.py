# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest06475():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})
