# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest80228():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
