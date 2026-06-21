# SPDX-License-Identifier: Apache-2.0
import os


request_state: dict[str, str] = {}

def BenchmarkTest26931():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
