# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest32376():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200
