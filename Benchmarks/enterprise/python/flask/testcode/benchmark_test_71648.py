# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def BenchmarkTest71648():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
