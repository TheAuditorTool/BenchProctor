# SPDX-License-Identifier: Apache-2.0
import logging
import re
import json
from flask import request, jsonify


def BenchmarkTest01145():
    raw_body = request.get_data(as_text=True)
    data = json.loads(raw_body).get('value', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
