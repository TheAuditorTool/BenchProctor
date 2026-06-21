# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest61884():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    os.seteuid(65534)
    return jsonify({"result": "success"})
