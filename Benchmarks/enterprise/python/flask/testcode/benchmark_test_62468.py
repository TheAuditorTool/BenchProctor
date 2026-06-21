# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest62468():
    msg_value = mq_client.get_message().body
    data = str(msg_value).replace('\x00', '')
    yaml.safe_load(data)
    return jsonify({"result": "success"})
