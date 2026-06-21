# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest37410():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
