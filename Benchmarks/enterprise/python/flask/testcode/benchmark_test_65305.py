# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65305():
    raw_body = request.get_data(as_text=True)
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
