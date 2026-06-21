# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35416():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
