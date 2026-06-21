# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import mq_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46352():
    msg_value = mq_client.get_message().body
    ctx = RequestContext(msg_value)
    data = ctx.payload
    json.loads(data)
    return jsonify({"result": "success"})
