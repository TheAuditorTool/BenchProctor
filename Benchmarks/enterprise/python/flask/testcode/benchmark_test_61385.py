# SPDX-License-Identifier: Apache-2.0
import threading
import base64
from flask import request, jsonify


def BenchmarkTest61385():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
