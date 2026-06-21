# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest73445():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    return jsonify({'error': 'An internal error occurred'}), 500
