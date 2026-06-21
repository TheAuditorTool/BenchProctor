# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest01161():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    requests.post('https://api.prod.internal/data', data=str(profile_value), verify=True)
    return jsonify({"result": "success"})
