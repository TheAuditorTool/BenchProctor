# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest18473():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
