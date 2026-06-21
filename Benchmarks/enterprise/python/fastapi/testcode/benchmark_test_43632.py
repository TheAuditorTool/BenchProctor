# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43632(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return {"updated": True}
