# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07175():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
