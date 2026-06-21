# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest20217():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
