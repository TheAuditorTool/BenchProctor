# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest68574():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    base_name = os.path.basename(str(forwarded_ip))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
