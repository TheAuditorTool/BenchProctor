# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest08968():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
