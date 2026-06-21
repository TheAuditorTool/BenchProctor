# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest78473():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
