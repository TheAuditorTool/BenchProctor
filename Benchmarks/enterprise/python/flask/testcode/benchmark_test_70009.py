# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest70009():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
