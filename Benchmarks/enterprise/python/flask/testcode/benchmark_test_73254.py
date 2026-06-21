# SPDX-License-Identifier: Apache-2.0


request_state: dict[str, str] = {}

def BenchmarkTest73254(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    return str(data), 200, {'Content-Type': 'text/html'}
