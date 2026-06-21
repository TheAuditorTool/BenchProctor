# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest02828():
    user_id = request.args.get('id', '')
    data = to_text(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
