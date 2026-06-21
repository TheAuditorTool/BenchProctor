# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48632():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
