# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42088():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
