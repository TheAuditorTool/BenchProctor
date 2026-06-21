# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest50332():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    random.seed(int(data) if str(data).isdigit() else 7)
    token = random.getrandbits(8)
    return jsonify({'token': str(token)}), 200
