# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle


def BenchmarkTest32920(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
