# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest63528():
    xml_value = request.get_data(as_text=True)
    reader = make_reader(xml_value)
    data = reader()
    return jsonify({'error': 'An internal error occurred'}), 500
