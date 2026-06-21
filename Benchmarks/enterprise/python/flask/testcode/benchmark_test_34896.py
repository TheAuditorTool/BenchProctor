# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest34896():
    auth_header = request.headers.get('Authorization', '')
    os.system('echo ' + str(auth_header))
    return jsonify({"result": "success"})
