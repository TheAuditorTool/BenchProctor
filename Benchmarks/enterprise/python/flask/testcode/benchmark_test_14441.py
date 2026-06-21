# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest14441(path_param):
    path_value = path_param
    data = default_blank(path_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
