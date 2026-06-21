# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest29116():
    xml_value = request.get_data(as_text=True)
    data = relay_value(xml_value)
    os.seteuid(65534)
    return jsonify({"result": "success"})
