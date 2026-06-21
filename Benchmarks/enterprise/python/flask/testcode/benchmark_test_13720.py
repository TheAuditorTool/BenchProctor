# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest13720():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
