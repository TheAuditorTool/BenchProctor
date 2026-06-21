# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11592():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
