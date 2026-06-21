# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest36183(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
