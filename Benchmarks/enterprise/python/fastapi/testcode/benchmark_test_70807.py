# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import shlex


async def BenchmarkTest70807(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
