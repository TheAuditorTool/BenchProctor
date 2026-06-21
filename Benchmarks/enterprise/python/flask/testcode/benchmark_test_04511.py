# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest04511():
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    importlib.import_module(str(data))
    return jsonify({"result": "success"})
