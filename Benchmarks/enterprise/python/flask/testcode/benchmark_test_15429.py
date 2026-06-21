# SPDX-License-Identifier: Apache-2.0
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest15429(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
