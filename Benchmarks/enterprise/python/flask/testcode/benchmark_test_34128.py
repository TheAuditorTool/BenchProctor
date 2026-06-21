# SPDX-License-Identifier: Apache-2.0
import json
from flask import jsonify
from app_runtime import mq_client


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest34128():
    msg_value = mq_client.get_message().body
    reader = make_reader(msg_value)
    data = reader()
    json.loads(data)
    return jsonify({"result": "success"})
