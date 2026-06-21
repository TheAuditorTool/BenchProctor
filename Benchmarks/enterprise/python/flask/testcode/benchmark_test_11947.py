# SPDX-License-Identifier: Apache-2.0
import random
import os
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest11947():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return jsonify({'token': str(token)}), 200
