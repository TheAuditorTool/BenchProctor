# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest39457():
    query_array = request.args.getlist('items')[0] if request.args.getlist('items') else ''
    data = FormData(payload=query_array).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
