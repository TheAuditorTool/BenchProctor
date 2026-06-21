# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def BenchmarkTest55291():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data, _sep, _rest = str(dotenv_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
