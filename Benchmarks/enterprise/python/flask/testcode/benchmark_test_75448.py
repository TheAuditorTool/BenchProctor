# SPDX-License-Identifier: Apache-2.0
import logging
import re
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest75448():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
