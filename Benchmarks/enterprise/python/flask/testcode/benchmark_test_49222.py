# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio
import ctypes


def BenchmarkTest49222(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
