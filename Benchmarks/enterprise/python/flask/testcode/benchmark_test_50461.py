# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest50461():
    xml_value = request.get_data(as_text=True)
    data = str(xml_value).replace('\x00', '')
    os.remove(str(data))
    return jsonify({"result": "success"})
