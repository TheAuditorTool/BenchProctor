# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest05890():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
