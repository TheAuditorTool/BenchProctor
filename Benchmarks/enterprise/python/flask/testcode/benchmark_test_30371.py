# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest30371(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
