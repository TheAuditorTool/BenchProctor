# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest37235():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
