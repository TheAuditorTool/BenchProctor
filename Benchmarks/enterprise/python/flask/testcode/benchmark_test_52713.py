# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest52713():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
