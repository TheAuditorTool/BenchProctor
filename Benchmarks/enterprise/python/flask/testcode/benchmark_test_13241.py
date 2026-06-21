# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest13241():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
