# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest12582():
    msg_value = mq_client.get_message().body
    def normalize(value):
        return value.strip()
    data = normalize(msg_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
