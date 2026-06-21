# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest44377():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
