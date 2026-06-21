# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest59689():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
