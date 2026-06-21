# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest73156():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
