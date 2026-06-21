# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest46182():
    xml_value = request.get_data(as_text=True)
    data = '%s' % (xml_value,)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
