# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest66061(path_param):
    path_value = path_param
    data = unquote(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
