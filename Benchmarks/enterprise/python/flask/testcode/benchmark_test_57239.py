# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest57239():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
