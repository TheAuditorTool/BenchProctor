# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04326():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
