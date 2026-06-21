# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest14570():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
