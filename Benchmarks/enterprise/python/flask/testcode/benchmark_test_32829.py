# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest32829():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
