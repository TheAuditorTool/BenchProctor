# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest04094():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % str(json_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
