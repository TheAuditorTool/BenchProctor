# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest00789():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
