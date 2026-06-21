# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest57455():
    stdin_value = input('input: ')
    with open('/var/app/data/' + str(stdin_value), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
