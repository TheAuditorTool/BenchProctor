# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest35265():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
