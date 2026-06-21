# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38357():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
