# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest37301():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
