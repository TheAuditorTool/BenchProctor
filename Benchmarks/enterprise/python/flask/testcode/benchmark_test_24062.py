# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest24062():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
