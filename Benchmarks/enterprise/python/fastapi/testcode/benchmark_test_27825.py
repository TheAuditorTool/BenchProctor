# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27825(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = str(config_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
