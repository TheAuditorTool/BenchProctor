# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest76730():
    origin_value = request.headers.get('Origin', '')
    os.remove(str(origin_value))
    return jsonify({"result": "success"})
