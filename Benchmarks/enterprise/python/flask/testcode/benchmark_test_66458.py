# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest66458():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    base_name = os.path.basename(str(json_value))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})
