# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest03545():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(dotenv_value))
    return jsonify({"result": "success"})
