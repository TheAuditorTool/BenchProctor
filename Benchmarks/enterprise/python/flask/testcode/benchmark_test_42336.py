# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest42336():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = forwarded_ip if forwarded_ip else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
