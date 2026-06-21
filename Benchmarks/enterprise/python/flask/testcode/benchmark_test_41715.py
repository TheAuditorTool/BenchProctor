# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest41715():
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
