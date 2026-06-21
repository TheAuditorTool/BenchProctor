# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest06334():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = json_value
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
