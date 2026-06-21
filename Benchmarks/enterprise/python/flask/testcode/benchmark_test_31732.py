# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31732():
    xml_value = request.get_data(as_text=True)
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
