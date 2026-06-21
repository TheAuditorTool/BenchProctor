# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48614():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
