# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13381():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
