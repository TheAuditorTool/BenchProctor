# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest03029():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
