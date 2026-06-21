# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09864():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
