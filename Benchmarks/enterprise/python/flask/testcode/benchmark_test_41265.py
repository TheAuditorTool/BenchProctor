# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest41265():
    upload_name = request.files['upload'].filename
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
