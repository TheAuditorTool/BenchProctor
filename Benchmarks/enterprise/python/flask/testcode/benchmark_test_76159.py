# SPDX-License-Identifier: Apache-2.0
import os
import re
import sys
from flask import jsonify


def BenchmarkTest76159():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
