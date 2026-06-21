# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest80987():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
