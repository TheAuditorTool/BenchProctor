# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest14743():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    os.remove(str(data))
    return jsonify({"result": "success"})
