# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest56431():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
