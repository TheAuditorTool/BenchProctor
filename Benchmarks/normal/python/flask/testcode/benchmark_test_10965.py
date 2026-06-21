# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest10965():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % (referer_value,)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
