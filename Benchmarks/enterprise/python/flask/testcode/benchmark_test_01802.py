# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest01802():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
