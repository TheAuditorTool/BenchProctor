# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest76490():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
