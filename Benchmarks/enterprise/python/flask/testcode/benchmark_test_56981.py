# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest56981():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    os.unlink('/var/app/data/' + str(forwarded_ip))
    return jsonify({"result": "success"})
