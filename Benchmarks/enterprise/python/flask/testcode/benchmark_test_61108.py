# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest61108(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
