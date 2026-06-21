# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import requests


async def BenchmarkTest19065(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    kind = 'json' if str(api_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = api_value
            data = parsed
        case _:
            data = api_value
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
