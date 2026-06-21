# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest47096():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = dotenv_value if dotenv_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
