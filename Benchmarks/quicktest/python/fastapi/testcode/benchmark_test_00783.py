# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest00783(request: Request):
    stdin_value = input('input: ')
    def normalize(value):
        return value.strip()
    data = normalize(stdin_value)
    os.system('echo ' + str(data))
    return {"updated": True}
