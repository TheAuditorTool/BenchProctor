# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest64018():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
