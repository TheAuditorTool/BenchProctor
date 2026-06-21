# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest60007():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    os.remove(str(data))
    return jsonify({"result": "success"})
