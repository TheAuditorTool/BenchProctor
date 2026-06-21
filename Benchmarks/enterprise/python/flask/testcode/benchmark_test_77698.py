# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest77698():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
