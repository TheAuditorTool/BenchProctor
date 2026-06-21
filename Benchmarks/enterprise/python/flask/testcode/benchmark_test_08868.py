# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest08868():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
