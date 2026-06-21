# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest27996():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
