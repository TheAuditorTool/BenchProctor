# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest37070():
    xml_value = request.get_data(as_text=True)
    data = (lambda v: v.strip())(xml_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
