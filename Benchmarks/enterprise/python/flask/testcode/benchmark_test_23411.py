# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest23411():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
