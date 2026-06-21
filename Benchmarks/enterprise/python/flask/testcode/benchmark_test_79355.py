# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import jsonify
import subprocess


def BenchmarkTest79355(path_param):
    path_value = path_param
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})
