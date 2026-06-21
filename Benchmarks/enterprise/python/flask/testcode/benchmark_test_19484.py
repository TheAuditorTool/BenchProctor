# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest19484():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    os.remove(str(data))
    return jsonify({"result": "success"})
