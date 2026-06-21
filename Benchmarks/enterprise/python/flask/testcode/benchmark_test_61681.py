# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61681():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}
