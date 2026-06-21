# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest12631():
    env_value = os.environ.get('USER_INPUT', '')
    defusedxml.ElementTree.fromstring(str(env_value))
    return jsonify({"result": "success"})
