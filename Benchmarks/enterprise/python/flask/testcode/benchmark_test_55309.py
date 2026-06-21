# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest55309(path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
