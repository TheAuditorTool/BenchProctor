# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05964():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = json_value
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
