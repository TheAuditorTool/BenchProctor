# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest41585():
    referer_value = request.headers.get('Referer', '')
    base_name = os.path.basename(str(referer_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
