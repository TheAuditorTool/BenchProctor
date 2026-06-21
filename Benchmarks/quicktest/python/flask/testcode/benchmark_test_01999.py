# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest01999():
    xml_value = request.get_data(as_text=True)
    data = xml_value if xml_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
