# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest57825(path_param):
    path_value = path_param
    logging.info('User action: ' + str(path_value))
    return jsonify({"result": "success"})
