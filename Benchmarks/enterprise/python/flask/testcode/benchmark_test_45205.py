# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest45205():
    upload_name = request.files['upload'].filename
    data = coalesce_blank(upload_name)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
