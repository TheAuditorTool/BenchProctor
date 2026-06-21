# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest19567(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
