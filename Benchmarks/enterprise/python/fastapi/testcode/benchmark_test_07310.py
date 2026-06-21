# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07310(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
