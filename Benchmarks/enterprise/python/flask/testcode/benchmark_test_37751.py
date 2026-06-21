# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest37751():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
