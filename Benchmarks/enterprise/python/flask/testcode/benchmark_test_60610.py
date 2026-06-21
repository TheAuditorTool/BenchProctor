# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest60610():
    msg_value = mq_client.get_message().body
    parts = str(msg_value).split(',')
    data = ','.join(parts)
    yaml.safe_load(data)
    return jsonify({"result": "success"})
