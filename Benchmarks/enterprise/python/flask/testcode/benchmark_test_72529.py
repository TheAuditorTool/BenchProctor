# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest72529():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
