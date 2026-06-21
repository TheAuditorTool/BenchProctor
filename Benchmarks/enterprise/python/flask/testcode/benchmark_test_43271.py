# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest43271():
    user_id = request.args.get('id', '')
    os.chmod('/var/app/data/' + str(user_id), 0o777)
    return jsonify({"result": "success"})
