# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest35396(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
