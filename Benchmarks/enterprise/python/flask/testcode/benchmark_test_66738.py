# SPDX-License-Identifier: Apache-2.0
import sys
from flask import jsonify


def BenchmarkTest66738():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = ' '.join(str(argv_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
