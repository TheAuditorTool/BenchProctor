# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest61670():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
