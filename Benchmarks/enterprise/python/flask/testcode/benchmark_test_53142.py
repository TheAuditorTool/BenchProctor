# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53142():
    referer_value = request.headers.get('Referer', '')
    if referer_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = referer_value
    eval(str(processed))
    return jsonify({"result": "success"})
