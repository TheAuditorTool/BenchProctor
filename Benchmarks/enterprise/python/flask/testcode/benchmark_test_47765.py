# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest47765(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
