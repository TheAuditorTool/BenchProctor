# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest72144(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
