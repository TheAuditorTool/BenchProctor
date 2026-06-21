# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest10285():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
