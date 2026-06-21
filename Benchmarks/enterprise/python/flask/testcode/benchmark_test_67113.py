# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest67113():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
