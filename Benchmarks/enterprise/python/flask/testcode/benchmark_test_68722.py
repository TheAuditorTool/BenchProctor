# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
from app_runtime import mq_client


def BenchmarkTest68722():
    msg_value = mq_client.get_message().body
    data, _sep, _rest = str(msg_value).partition('\x00')
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
