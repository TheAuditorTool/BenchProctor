# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest39771(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
