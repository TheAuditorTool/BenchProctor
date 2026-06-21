# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest37976():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
