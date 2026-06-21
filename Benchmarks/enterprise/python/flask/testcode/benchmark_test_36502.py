# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest36502():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
