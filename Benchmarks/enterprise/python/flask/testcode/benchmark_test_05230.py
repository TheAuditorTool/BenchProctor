# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify


def BenchmarkTest05230(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    session['data'] = str(data)
    return jsonify({"result": "success"})
