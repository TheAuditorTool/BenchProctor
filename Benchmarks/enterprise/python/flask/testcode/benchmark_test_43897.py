# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest43897():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})
