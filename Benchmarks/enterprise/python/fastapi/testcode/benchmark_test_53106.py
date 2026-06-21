# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import requests


async def BenchmarkTest53106(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = api_value if api_value else 'default'
    yaml.safe_load(data)
    return {"updated": True}
