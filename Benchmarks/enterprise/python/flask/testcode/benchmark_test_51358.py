# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest51358():
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    json.loads(data)
    return jsonify({"result": "success"})
