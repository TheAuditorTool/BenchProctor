# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09119():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
