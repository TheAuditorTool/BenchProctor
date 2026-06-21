# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest23674(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
