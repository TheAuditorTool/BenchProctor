# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest20352():
    user_id = request.args.get('id', '')
    logging.info('User action: ' + str(user_id))
    return jsonify({"result": "success"})
