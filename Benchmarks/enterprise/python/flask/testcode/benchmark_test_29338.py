# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29338():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})
