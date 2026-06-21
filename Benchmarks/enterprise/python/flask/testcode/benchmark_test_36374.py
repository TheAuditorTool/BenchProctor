# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest36374(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
