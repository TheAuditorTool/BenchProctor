# SPDX-License-Identifier: Apache-2.0
from flask import session
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest57894(path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    session['data'] = str(data)
    return jsonify({"result": "success"})
