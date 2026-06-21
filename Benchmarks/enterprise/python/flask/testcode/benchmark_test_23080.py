# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest23080():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
