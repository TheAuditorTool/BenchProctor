# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import time


def BenchmarkTest54809():
    xml_value = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})
