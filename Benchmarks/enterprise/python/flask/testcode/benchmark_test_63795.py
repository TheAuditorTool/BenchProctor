# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest63795():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
