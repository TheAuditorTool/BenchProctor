# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest48906():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
