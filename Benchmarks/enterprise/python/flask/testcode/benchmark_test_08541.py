# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest08541(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
