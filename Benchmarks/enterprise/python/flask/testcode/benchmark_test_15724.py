# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest15724():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    os.chmod('/var/app/data/' + str(forwarded_ip), 0o777)
    return jsonify({"result": "success"})
