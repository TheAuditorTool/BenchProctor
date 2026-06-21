# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest43445():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    os.remove(str(data))
    return jsonify({"result": "success"})
