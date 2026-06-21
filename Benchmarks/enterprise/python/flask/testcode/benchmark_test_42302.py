# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import subprocess


def BenchmarkTest42302():
    multipart_value = request.form.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = multipart_value
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
