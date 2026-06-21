# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest36769():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
