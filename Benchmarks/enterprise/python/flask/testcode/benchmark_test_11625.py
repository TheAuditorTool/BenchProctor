# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest11625():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
