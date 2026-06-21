# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest35493(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
