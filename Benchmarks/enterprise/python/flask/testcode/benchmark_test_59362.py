# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest59362():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    os.seteuid(65534)
    return jsonify({"result": "success"})
