# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59978():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
