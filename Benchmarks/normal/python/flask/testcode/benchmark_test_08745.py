# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest08745():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
