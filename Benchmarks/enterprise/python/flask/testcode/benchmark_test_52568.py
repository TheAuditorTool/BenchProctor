# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest52568():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
