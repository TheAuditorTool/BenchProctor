# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle


def BenchmarkTest67432(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
