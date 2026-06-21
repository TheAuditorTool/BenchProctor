# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest43368():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
