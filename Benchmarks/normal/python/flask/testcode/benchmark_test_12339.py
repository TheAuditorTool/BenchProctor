# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest12339():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
