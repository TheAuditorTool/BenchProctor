# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest74362():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
