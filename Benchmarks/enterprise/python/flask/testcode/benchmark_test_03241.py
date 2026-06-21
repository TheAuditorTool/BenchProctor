# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03241():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
