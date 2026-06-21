# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest58952():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
