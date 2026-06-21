# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest55920():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
