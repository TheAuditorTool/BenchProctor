# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify


def BenchmarkTest08163(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
