# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest60890():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})
