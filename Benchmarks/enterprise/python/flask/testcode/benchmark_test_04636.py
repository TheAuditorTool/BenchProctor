# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest04636():
    ua_value = request.headers.get('User-Agent', '')
    base_name = os.path.basename(str(ua_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
