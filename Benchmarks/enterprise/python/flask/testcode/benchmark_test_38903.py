# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest38903():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = RequestPayload(secret_value).value
    auth_check('user', data)
    return jsonify({"result": "success"})
