# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def BenchmarkTest44740():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    logging.info('User action: ' + str(dotenv_value))
    return jsonify({"result": "success"})
