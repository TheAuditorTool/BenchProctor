# SPDX-License-Identifier: Apache-2.0
import threading
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest63084():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
