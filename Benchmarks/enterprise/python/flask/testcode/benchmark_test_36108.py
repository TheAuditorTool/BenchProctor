# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest36108():
    xml_value = request.get_data(as_text=True)
    data = normalise_input(xml_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
