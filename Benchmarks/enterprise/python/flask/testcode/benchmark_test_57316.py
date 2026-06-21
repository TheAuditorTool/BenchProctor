# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57316():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
