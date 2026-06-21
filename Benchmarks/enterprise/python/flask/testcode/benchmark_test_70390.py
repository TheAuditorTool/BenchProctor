# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest70390():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
