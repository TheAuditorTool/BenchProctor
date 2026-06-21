# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest12165():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
