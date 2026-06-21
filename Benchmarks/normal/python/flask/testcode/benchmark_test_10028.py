# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest10028():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
