# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest01243(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
