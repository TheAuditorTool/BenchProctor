# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40762(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % str(config_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
