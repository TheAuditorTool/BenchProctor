# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest53447():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
