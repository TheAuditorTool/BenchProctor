# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest36665():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
