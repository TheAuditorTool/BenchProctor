# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest15913():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    auth_check('user', data)
    return jsonify({"result": "success"})
