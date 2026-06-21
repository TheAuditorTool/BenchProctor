# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23140():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}
