# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest08362():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
