# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest09964(path_param):
    path_value = path_param
    defusedxml.ElementTree.fromstring(str(path_value))
    return jsonify({"result": "success"})
