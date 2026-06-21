# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest74319():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    requests.post('http://api.prod.internal/data', data=str(profile_value))
    return jsonify({"result": "success"})
