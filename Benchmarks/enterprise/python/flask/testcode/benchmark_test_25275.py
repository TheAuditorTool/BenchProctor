# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import mq_client


def BenchmarkTest25275():
    msg_value = mq_client.get_message().body
    data = (lambda v: v.strip())(msg_value)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
