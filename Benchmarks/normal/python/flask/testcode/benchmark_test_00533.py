# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00533():
    host_value = request.headers.get('Host', '')
    base_name = os.path.basename(str(host_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
