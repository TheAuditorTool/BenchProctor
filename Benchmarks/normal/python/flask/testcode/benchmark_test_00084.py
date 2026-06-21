# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest00084():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
