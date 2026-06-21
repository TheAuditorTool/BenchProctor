# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os


def BenchmarkTest80802():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % (dotenv_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
