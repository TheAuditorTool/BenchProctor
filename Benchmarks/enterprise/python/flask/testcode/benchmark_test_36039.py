# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest36039():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
