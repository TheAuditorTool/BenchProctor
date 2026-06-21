# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest51894(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
