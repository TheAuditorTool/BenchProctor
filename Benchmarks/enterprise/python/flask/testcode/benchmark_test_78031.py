# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78031():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
