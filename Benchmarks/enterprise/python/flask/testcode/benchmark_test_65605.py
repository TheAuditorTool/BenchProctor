# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest65605():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
