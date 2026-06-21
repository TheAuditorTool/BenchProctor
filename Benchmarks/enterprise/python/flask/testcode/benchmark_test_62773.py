# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest62773():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
