# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest47538():
    field_value = request.form.get('field', '')
    data = normalise_input(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
