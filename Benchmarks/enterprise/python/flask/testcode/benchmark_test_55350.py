# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest55350():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
