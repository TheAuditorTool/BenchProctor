# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
import sys
from flask import jsonify


def BenchmarkTest14215():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    parts = str(argv_value).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
