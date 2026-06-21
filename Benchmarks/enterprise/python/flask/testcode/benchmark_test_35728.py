# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest35728():
    raw_body = request.get_data(as_text=True)
    logging.info('User action: ' + str(raw_body))
    return jsonify({"result": "success"})
