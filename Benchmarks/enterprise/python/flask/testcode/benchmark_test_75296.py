# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest75296():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
