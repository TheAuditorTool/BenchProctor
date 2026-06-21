# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time
import ast


def BenchmarkTest40992():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
