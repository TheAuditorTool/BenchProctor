# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45413():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
