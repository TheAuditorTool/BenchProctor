# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03586():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
