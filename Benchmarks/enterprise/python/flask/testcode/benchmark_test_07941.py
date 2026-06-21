# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest07941():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
