# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest41473():
    auth_header = request.headers.get('Authorization', '')
    data = '{}'.format(auth_header)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
