# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest41856():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
