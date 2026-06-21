# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06124():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200
