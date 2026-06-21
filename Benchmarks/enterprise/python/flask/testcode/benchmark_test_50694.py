# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest50694():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
