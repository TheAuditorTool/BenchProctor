# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import requests
import json


async def BenchmarkTest16628(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    try:
        data = json.loads(api_value).get('value', api_value)
    except (json.JSONDecodeError, AttributeError):
        data = api_value
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
