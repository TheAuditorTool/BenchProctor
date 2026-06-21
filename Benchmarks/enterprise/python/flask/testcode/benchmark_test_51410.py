# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest51410():
    host_value = request.headers.get('Host', '')
    reader = make_reader(host_value)
    data = reader()
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
