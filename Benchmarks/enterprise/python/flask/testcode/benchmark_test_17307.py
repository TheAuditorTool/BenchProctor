# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest17307(path_param):
    path_value = path_param
    data = unquote(path_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
