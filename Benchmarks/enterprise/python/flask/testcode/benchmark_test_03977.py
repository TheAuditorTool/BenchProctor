# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import json
import os


def BenchmarkTest03977():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
