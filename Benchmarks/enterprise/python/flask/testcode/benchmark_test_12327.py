# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest12327():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = []
    for token in str(profile_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
