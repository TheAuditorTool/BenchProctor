# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest53416():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
