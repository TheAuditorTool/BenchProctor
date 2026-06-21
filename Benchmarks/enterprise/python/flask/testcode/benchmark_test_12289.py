# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest12289():
    referer_value = request.headers.get('Referer', '')
    reader = make_reader(referer_value)
    data = reader()
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
