# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00701():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
