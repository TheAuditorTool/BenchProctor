# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest31243():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    os.seteuid(65534)
    return jsonify({"result": "success"})
