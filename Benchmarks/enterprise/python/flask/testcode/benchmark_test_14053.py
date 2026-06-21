# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest14053():
    xml_value = request.get_data(as_text=True)
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
