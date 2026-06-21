# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def ensure_str(value):
    return str(value)

def BenchmarkTest13191():
    user_id = request.args.get('id', '')
    data = ensure_str(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
