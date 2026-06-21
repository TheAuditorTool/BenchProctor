# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os


def BenchmarkTest51581():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    kind = 'json' if str(dotenv_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = dotenv_value
            data = parsed
        case _:
            data = dotenv_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
