# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


def normalise_input(value):
    return value.strip()

async def BenchmarkTest21966(request: Request):
    stdin_value = input('input: ')
    data = normalise_input(stdin_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
