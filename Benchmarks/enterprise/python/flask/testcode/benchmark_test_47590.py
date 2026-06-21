# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest47590():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
