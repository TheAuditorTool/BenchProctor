# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest03453(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
