# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04426():
    ua_value = request.headers.get('User-Agent', '')
    os.remove(str(ua_value))
    return jsonify({"result": "success"})
