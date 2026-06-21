# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest29149():
    xml_value = request.get_data(as_text=True)
    data = '%s' % str(xml_value)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
