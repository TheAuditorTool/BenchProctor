# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest24126():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
