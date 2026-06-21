# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


def BenchmarkTest74133():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '%s' % str(profile_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
