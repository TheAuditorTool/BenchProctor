# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77484():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
