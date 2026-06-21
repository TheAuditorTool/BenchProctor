# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03581():
    ua_value = request.headers.get('User-Agent', '')
    data = RequestPayload(ua_value).value
    yaml.safe_load(data)
    return jsonify({"result": "success"})
