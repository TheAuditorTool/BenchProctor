# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest23978(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
