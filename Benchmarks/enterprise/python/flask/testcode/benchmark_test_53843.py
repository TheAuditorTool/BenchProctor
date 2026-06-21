# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest53843():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
