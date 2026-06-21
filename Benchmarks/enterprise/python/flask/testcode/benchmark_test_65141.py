# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest65141():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(profile_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
