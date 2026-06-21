# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19804():
    referer_value = request.headers.get('Referer', '')
    data = '{}'.format(referer_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})
