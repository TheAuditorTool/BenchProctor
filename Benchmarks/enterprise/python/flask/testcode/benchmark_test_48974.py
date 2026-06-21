# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest48974():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
