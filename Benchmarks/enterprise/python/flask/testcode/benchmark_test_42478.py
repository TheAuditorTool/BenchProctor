# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def relay_value(value):
    return value

def BenchmarkTest42478():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = relay_value(dotenv_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
