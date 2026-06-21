# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest73926():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
