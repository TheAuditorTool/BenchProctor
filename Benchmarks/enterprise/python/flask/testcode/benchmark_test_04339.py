# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import jsonify
import pickle
from app_runtime import mq_client


@dataclass
class FormData:
    payload: str

def BenchmarkTest04339():
    msg_value = mq_client.get_message().body
    data = FormData(payload=msg_value).payload
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
