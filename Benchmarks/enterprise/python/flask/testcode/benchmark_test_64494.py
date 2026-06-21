# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest64494():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = RequestPayload(profile_value).value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
