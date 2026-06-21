# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06252():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
