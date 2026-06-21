# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest02679():
    xml_value = request.get_data(as_text=True)
    data = RequestPayload(xml_value).value
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
