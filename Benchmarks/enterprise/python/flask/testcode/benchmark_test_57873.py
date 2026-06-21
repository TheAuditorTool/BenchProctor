# SPDX-License-Identifier: Apache-2.0
import sys
from flask import jsonify


def BenchmarkTest57873():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = '%s' % str(argv_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
