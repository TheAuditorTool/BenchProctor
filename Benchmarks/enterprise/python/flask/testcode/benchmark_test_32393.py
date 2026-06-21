# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest32393():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    os.seteuid(65534)
    return jsonify({"result": "success"})
