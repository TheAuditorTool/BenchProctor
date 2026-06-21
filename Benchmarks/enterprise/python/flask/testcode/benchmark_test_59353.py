# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest59353():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
