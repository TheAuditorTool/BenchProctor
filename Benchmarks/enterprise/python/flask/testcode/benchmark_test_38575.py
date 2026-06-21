# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def coalesce_blank(value):
    return value or ''

def BenchmarkTest38575():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    eval(compile("pickle.loads(data.encode('latin-1'))", '<sink>', 'exec'))
    return jsonify({"result": "success"})
