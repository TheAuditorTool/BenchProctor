# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def BenchmarkTest78249():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = str(dotenv_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
