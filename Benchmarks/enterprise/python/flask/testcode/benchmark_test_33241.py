# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest33241():
    auth_header = request.headers.get('Authorization', '')
    os.remove(str(auth_header))
    return jsonify({"result": "success"})
