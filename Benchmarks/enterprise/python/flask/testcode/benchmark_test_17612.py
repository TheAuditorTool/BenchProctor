# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest17612():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
