# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest10215():
    user_id = request.args.get('id', '')
    defusedxml.ElementTree.fromstring(str(user_id))
    return jsonify({"result": "success"})
