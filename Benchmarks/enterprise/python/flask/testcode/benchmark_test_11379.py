# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest11379():
    xml_value = request.get_data(as_text=True)
    os.remove(str(xml_value))
    return jsonify({"result": "success"})
