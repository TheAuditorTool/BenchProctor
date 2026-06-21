# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest44867():
    ua_value = request.headers.get('User-Agent', '')
    reader = make_reader(ua_value)
    data = reader()
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
