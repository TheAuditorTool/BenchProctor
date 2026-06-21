# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest33284():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})
