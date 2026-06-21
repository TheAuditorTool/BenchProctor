# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest43753():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return jsonify({"result": "success"})
