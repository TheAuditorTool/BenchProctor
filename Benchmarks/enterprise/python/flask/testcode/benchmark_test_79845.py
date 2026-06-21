# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest79845():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
