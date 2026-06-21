# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest22697(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
