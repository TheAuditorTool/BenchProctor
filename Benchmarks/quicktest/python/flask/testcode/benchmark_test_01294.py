# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest01294(path_param):
    path_value = path_param
    data = relay_value(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
