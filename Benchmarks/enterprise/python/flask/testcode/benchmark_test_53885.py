# SPDX-License-Identifier: Apache-2.0
import os
import re
from urllib.parse import unquote
from flask import request, jsonify
import subprocess


def BenchmarkTest53885():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
