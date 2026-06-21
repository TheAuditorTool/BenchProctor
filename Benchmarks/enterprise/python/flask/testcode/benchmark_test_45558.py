# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest45558():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
