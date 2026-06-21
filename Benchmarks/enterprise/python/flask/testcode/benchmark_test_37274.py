# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest37274(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
