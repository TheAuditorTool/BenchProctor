# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest65682():
    msg_value = mq_client.get_message().body
    data = (lambda v: v.strip())(msg_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
