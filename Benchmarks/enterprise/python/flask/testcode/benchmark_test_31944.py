# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import jsonify


def BenchmarkTest31944(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
