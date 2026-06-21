# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest34074():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
