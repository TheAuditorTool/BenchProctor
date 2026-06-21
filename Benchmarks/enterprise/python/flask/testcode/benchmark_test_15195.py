# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest15195():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
