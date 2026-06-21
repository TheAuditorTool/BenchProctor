# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest02264():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})
