# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest24266():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    os.remove(str(data))
    return jsonify({"result": "success"})
