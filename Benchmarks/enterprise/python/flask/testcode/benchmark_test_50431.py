# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest50431(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
