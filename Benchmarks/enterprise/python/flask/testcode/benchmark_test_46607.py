# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest46607():
    upload_name = request.files['upload'].filename
    logging.info('User action: ' + str(upload_name))
    return jsonify({"result": "success"})
