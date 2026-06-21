# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest28473():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
