# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest21663():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
