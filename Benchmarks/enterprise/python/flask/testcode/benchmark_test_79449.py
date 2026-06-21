# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest79449():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
