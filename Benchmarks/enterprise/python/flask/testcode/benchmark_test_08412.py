# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest08412():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
