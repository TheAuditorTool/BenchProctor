# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest31875():
    stdin_value = input('input: ')
    pending = list(str(stdin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
