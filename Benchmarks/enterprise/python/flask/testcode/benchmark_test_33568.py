# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest33568():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
