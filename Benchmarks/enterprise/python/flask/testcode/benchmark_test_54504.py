# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest54504():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
