# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest11422():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})
