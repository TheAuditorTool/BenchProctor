# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest35433():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
