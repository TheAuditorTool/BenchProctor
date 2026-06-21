# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00802():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
