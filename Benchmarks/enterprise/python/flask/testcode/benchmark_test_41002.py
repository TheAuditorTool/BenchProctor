# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest41002():
    referer_value = request.headers.get('Referer', '')
    data = RequestPayload(referer_value).value
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
