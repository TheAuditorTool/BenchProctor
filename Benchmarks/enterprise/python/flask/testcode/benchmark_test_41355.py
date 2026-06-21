# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest41355():
    user_id = request.args.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
