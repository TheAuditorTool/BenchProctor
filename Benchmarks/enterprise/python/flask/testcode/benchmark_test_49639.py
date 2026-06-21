# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest49639():
    auth_header = request.headers.get('Authorization', '')
    data = coalesce_blank(auth_header)
    os.remove(str(data))
    return jsonify({"result": "success"})
