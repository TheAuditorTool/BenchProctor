# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest16891():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
