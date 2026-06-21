# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest56689():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
