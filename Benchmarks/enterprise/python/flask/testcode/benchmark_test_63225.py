# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest63225():
    xml_value = request.get_data(as_text=True)
    data = ' '.join(str(xml_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
