# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest53143():
    origin_value = request.headers.get('Origin', '')
    reader = make_reader(origin_value)
    data = reader()
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
