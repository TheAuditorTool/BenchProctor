# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest27974():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = FormData(payload=prop_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
