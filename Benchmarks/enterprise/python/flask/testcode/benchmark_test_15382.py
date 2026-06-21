# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest15382():
    user_id = request.args.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
