# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import jsonify


def BenchmarkTest20052(path_param):
    path_value = path_param
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(path_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
