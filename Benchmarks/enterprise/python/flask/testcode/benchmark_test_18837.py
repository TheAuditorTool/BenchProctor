# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest18837():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
