# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest49977():
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})
