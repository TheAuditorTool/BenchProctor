# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest67751():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
