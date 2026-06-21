# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import defusedxml.ElementTree


def BenchmarkTest58177():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
