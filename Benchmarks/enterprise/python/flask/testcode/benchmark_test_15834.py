# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest15834():
    msg_value = mq_client.get_message().body
    parts = str(msg_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return jsonify({"result": "success"})
