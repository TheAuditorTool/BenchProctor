# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import requests


async def BenchmarkTest29466(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    parts = []
    for token in str(api_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    yaml.safe_load(data)
    return {"updated": True}
