# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest69719():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
