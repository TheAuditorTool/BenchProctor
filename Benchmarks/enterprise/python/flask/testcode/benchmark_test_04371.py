# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04371():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
