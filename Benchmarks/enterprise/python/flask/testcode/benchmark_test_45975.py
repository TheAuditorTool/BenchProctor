# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45975():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
