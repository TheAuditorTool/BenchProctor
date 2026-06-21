# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest23056():
    xml_value = request.get_data(as_text=True)
    logging.info('User action: ' + str(xml_value))
    return jsonify({"result": "success"})
