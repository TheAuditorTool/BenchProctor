# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest71256():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
