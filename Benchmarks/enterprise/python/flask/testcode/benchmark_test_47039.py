# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47039():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
