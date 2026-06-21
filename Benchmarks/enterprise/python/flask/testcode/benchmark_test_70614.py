# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest70614(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
