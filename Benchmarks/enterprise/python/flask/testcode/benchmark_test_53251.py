# SPDX-License-Identifier: Apache-2.0
import os
import sys
from flask import jsonify


def BenchmarkTest53251():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return jsonify({"result": "success"})
