# SPDX-License-Identifier: Apache-2.0
import yaml
from dataclasses import dataclass
from flask import jsonify
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest06388():
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})
