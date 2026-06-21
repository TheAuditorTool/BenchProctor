# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
from app_runtime import mq_client


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest35567():
    msg_value = mq_client.get_message().body
    data = RequestPayload(msg_value).value
    requests.get(str(data))
    return jsonify({"result": "success"})
