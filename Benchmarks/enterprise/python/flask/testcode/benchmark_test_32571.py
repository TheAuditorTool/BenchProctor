# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest32571(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
