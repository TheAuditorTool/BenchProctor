# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest79224(path_param):
    path_value = path_param
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(path_value))
    return jsonify({"result": "success"})
