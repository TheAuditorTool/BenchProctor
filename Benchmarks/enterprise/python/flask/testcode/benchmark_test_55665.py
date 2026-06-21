# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest55665():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
