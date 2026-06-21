# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def normalise_input(value):
    return value.strip()

def BenchmarkTest29418(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
