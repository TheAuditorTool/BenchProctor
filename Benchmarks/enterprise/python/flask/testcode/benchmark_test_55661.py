# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest55661():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    data = FormData(payload=yaml_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
