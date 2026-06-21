# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest23018():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
