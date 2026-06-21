# SPDX-License-Identifier: Apache-2.0
import logging
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest11656():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
