# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest38851():
    field_value = request.form.get('field', '')
    data = FormData(payload=field_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
