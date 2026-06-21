# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest47570():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
