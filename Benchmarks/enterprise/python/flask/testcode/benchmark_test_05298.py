# SPDX-License-Identifier: Apache-2.0
import os
import re
import json
from flask import request, jsonify
import subprocess


def BenchmarkTest05298():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
