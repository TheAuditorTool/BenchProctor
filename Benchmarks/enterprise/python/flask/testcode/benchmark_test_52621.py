# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest52621():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ' '.join(str(header_value).split())
    os.seteuid(65534)
    return jsonify({"result": "success"})
