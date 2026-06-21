# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26148():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
