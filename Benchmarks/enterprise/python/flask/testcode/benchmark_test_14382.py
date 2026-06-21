# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest14382():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
