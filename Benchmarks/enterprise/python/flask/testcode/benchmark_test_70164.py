# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest70164():
    xml_value = request.get_data(as_text=True)
    os.system('echo ' + str(xml_value))
    return jsonify({"result": "success"})
