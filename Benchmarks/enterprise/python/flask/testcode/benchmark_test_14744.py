# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest14744():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
