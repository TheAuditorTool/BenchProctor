# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest25173(path_param):
    path_value = path_param
    data = unquote(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
