# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40657():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
