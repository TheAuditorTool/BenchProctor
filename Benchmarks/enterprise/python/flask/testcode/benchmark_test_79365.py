# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest79365():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
