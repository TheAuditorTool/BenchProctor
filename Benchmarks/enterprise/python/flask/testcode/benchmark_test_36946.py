# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest36946():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
