# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest03408(path_param):
    path_value = path_param
    data = f'{path_value}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
