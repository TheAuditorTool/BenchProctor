# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest46420():
    referer_value = request.headers.get('Referer', '')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(referer_value).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
