# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest81299():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    os.remove(str(data))
    return jsonify({"result": "success"})
