# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest33161():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
