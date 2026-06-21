# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest51841():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    int(str(data))
    return jsonify({"result": "success"})
