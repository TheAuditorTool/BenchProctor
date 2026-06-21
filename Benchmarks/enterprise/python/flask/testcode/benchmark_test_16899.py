# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest16899():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
