# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest12893():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
