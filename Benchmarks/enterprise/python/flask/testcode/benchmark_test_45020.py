# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45020():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    return jsonify({'error': 'An internal error occurred'}), 500
