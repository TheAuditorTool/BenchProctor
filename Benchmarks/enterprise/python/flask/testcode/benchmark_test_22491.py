# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest22491():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
