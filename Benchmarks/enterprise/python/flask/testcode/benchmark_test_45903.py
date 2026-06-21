# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import time


def ensure_str(value):
    return str(value)

def BenchmarkTest45903(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
