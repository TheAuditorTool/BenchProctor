# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest33786():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    os.remove(str(data))
    return jsonify({"result": "success"})
