# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import json
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest67984():
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    json.loads(data)
    return jsonify({"result": "success"})
