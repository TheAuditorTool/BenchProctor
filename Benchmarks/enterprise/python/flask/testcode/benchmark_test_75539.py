# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest75539():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
