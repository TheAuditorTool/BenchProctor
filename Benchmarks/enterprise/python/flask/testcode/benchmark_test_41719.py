# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest41719():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
