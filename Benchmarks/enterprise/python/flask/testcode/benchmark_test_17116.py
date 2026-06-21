# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17116():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
