# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest45715():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
