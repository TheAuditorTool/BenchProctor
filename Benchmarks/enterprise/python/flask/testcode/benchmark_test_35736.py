# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35736():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
