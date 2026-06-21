# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest25529():
    user_id = request.args.get('id', '')
    if user_id not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = user_id
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
