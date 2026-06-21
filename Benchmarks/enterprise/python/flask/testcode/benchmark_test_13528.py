# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import jsonify
from types import SimpleNamespace


def BenchmarkTest13528(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
