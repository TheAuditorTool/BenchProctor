# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest40478():
    host_value = request.headers.get('Host', '')
    defusedxml.ElementTree.fromstring(str(host_value))
    return jsonify({"result": "success"})
