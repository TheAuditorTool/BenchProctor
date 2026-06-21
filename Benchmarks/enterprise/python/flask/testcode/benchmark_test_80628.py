# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80628():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
