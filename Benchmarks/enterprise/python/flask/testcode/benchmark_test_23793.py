# SPDX-License-Identifier: Apache-2.0
import os
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest23793():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
