# SPDX-License-Identifier: Apache-2.0
import sys
from flask import jsonify


def BenchmarkTest22754():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = str(argv_value).replace('\x00', '')
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
