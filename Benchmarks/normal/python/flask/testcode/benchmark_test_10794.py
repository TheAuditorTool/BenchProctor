# SPDX-License-Identifier: Apache-2.0
import yaml
import json
import os
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest10794():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    yaml.safe_load(data)
    return jsonify({"result": "success"})
