# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest22164():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
