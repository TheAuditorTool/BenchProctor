# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest81387():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
