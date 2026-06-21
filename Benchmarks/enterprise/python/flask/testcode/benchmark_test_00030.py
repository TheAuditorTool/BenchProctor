# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00030():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
