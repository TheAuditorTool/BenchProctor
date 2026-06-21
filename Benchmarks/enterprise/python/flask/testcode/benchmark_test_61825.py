# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest61825():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
