# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest07711():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
