# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest03838():
    stdin_value = input('input: ')
    data = FormData(payload=stdin_value).payload
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
