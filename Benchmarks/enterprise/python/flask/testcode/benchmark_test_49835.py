# SPDX-License-Identifier: Apache-2.0
import requests
import json
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest49835():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
