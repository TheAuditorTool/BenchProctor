# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest79556(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
