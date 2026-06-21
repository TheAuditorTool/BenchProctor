# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest14016():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '{}'.format(profile_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
