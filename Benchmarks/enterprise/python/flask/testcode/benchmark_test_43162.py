# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest43162(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
