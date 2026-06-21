# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify


def BenchmarkTest11312():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
