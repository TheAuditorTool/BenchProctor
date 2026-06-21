# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09569():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
