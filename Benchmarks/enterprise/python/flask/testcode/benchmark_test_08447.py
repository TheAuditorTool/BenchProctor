# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
import os
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest08447():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
