# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest19719():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
