# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest49857():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
