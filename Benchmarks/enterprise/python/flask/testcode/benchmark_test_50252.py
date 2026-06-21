# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest50252():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
