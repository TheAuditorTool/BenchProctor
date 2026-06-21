# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest59019():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
