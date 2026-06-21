# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest14311():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
