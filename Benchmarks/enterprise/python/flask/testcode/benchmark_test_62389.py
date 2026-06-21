# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest62389():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
