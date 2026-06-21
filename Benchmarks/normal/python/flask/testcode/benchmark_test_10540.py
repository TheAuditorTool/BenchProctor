# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest10540():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
