# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest79756():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
