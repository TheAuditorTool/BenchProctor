# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03000():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
