# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest37320():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    return jsonify({'error': 'An internal error occurred'}), 500
