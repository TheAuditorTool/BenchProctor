# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest23734():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
