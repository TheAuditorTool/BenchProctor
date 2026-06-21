# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest72686():
    xml_value = request.get_data(as_text=True)
    data = FormData(payload=xml_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
