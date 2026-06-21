# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest81209():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
