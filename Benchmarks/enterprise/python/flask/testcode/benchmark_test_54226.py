# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest54226():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
