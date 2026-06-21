# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest12657():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
