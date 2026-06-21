# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09735():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
