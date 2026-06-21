# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09159():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
