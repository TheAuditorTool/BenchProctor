# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest43843(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
