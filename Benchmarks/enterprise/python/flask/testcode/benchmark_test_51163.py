# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest51163(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
