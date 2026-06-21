# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest41438():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
