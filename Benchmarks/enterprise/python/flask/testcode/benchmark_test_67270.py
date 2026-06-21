# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest67270():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
