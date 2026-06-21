# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest61480():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
