# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest18448():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
