# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52712():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
