# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest80971():
    field_value = request.form.get('field', '')
    logging.info('User action: ' + str(field_value))
    return jsonify({"result": "success"})
