# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest22699(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    request_state['last_input'] = api_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return {"updated": True}
