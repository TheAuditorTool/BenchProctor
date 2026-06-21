# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest13232():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = str(profile_value).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
