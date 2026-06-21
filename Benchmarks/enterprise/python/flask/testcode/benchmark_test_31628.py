# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest31628(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
