# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58150():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    exec(str(data))
    return jsonify({"result": "success"})
