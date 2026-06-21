# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest14730():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
