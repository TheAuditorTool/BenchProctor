# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest18178():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
