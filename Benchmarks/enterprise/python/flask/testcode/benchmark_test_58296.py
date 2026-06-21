# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import pickle
from app_runtime import mq_client


def BenchmarkTest58296():
    msg_value = mq_client.get_message().body
    pending = list(str(msg_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})
