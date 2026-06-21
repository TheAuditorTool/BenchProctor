# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest12940(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
