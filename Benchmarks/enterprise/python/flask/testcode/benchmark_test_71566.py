# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest71566():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = ' '.join(str(dotenv_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
