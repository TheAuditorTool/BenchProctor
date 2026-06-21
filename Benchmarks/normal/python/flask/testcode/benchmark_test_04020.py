# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest04020():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
