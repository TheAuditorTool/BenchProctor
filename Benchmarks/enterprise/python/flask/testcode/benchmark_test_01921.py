# SPDX-License-Identifier: Apache-2.0
import logging
from dataclasses import dataclass
from flask import jsonify
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest01921(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
