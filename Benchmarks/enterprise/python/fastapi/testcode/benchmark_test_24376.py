# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest24376(request: Request):
    stdin_value = input('input: ')
    def normalize(value):
        return value.strip()
    data = normalize(stdin_value)
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
