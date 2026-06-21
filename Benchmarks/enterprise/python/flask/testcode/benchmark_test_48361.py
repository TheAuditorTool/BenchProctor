# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest48361():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ctx = RequestContext(profile_value)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
