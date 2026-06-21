# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest01438():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
