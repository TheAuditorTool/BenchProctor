# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time


def normalise_input(value):
    return value.strip()

def BenchmarkTest34734():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return jsonify({"result": "success"})
