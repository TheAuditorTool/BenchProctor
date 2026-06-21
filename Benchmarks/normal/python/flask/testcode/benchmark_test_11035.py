# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest11035():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
