# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest36795():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
