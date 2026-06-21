# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
import sys
from flask import jsonify


def BenchmarkTest74181():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
