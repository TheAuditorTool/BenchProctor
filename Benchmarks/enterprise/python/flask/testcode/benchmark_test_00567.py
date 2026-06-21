# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import jsonify
import ast
from app_runtime import mq_client


def BenchmarkTest00567():
    msg_value = mq_client.get_message().body
    try:
        data = str(ast.literal_eval(msg_value))
    except (ValueError, SyntaxError):
        data = msg_value
    yaml.safe_load(data)
    return jsonify({"result": "success"})
