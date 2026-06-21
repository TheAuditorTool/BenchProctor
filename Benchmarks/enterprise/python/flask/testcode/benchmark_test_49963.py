# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest49963(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
