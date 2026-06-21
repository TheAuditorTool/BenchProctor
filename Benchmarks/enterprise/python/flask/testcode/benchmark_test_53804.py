# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest53804():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
