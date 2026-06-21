# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest28397():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
