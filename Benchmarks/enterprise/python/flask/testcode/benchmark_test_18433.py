# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest18433():
    raw_body = request.get_data(as_text=True)
    data = '%s' % (raw_body,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
