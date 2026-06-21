# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest59838():
    stdin_value = input('input: ')
    data = ' '.join(str(stdin_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
