# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest25205():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    int(str(data))
    return jsonify({"result": "success"})
