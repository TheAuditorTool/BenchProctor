# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest18243():
    user_id = request.args.get('id', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(user_id).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
