# SPDX-License-Identifier: Apache-2.0
import subprocess
import json
from flask import request, jsonify


def BenchmarkTest04615():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
