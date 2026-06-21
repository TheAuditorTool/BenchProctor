# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest31740(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
