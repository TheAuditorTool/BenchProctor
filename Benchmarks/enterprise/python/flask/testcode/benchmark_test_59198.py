# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest59198(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
