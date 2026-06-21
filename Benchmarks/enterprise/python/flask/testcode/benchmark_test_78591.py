# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest78591():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
