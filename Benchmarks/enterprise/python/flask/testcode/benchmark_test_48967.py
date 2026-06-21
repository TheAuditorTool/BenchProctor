# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
import defusedxml.ElementTree


def BenchmarkTest48967():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
