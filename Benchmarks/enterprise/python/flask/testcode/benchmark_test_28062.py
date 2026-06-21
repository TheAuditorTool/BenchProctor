# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28062():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
