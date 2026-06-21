# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest13455():
    msg_value = mq_client.get_message().body
    data = f'{msg_value:.200s}'
    requests.get(str(data))
    return jsonify({"result": "success"})
