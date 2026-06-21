# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest73001():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = json.loads(profile_value).get('value', profile_value)
    except (json.JSONDecodeError, AttributeError):
        data = profile_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
