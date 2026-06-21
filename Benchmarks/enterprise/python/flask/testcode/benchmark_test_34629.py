# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def BenchmarkTest34629():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = str(dotenv_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
