# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify


def BenchmarkTest46645():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value:.200s}'
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
