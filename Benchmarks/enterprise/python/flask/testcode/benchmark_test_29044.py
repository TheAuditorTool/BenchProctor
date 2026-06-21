# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest29044():
    xml_value = request.get_data(as_text=True)
    data = '{}'.format(xml_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
