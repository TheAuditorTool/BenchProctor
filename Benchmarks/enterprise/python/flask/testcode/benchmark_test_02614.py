# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02614():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
