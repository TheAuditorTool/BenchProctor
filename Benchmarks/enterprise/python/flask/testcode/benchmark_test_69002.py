# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest69002():
    user_id = request.args.get('id', '')
    os.remove(str(user_id))
    return jsonify({"result": "success"})
