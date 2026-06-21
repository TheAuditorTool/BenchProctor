# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import sys


async def BenchmarkTest35637(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = ' '.join(str(argv_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
