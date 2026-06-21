# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00306():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})
