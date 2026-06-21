# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import request, jsonify
import subprocess


def BenchmarkTest67725():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
