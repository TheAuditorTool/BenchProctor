# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest04469():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    json.loads(data)
    return jsonify({"result": "success"})
