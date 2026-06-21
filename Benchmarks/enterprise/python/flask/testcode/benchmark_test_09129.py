# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest09129():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    os.seteuid(65534)
    return jsonify({"result": "success"})
