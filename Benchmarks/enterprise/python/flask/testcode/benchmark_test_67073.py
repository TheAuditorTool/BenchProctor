# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest67073():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
