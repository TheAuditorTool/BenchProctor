# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest39655(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
