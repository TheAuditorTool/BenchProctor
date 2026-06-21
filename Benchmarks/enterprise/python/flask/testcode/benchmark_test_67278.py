# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest67278():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
