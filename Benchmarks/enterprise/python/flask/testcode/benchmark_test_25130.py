# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest25130():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
