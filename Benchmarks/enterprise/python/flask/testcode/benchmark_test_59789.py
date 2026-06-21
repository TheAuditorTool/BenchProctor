# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
import defusedxml.ElementTree


def BenchmarkTest59789(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
