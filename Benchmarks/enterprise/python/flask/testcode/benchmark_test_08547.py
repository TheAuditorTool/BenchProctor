# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest08547(path_param):
    path_value = path_param
    data = f'{path_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
