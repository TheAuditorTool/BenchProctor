# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest13428(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
