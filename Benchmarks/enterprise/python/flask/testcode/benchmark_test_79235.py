# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest79235():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    os.remove(str(data))
    return jsonify({"result": "success"})
