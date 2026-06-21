# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest71904(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
