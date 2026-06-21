# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest64723():
    raw_body = request.get_data(as_text=True)
    defusedxml.ElementTree.fromstring(str(raw_body))
    return jsonify({"result": "success"})
