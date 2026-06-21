# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest40810(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
