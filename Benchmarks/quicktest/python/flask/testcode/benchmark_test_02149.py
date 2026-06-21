# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import mq_client


request_state: dict[str, str] = {}

def BenchmarkTest02149():
    msg_value = mq_client.get_message().body
    request_state['last_input'] = msg_value
    data = request_state['last_input']
    yaml.safe_load(data)
    return jsonify({"result": "success"})
