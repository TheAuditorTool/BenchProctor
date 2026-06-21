# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09461():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
