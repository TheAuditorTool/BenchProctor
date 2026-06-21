# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03317():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})
