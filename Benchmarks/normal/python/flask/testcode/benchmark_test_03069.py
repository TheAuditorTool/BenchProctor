# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03069():
    xml_value = request.get_data(as_text=True)
    data = RequestPayload(xml_value).value
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
