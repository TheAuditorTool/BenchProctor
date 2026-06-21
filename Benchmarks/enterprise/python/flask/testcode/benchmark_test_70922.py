# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest70922():
    secret_value = 'config_secret_test_abc123'
    data = RequestPayload(secret_value).value
    auth_check('user', data)
    return jsonify({"result": "success"})
