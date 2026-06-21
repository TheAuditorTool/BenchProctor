# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52787():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
