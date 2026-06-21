# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest39753():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % (forwarded_ip,)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
