# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest26952():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
