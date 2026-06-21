# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest69248():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    os.chmod('/var/app/data/' + str(json_value), 0o777)
    return jsonify({"result": "success"})
