# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest73035(request: Request):
    user_id = request.query_params.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
