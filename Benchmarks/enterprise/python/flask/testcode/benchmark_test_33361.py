# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest33361():
    msg_value = mq_client.get_message().body
    data = '{}'.format(msg_value)
    requests.get(str(data))
    return jsonify({"result": "success"})
