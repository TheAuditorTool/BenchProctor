# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80241():
    xml_value = request.get_data(as_text=True)
    parts = []
    for token in str(xml_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
