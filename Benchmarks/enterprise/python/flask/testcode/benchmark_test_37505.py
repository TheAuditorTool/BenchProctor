# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest37505():
    user_id = request.args.get('id', '')
    data = default_blank(user_id)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
