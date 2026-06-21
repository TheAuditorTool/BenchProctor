# SPDX-License-Identifier: Apache-2.0
import logging
import re
from flask import request, jsonify


def BenchmarkTest64837():
    upload_name = request.files['upload'].filename
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return jsonify({'error': 'forbidden'}), 400
    processed = upload_name
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
