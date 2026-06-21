# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest42810():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
