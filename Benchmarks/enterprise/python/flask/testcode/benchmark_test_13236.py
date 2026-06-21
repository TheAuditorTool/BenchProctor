# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest13236():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = profile_value if profile_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
