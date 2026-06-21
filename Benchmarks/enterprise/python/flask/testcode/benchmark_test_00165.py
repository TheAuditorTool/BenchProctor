# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00165():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = FormData(payload=config_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
