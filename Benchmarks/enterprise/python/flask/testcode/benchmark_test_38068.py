# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


def BenchmarkTest38068():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
