# SPDX-License-Identifier: Apache-2.0


request_state: dict[str, str] = {}

def BenchmarkTest54915(path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = content", '<sink>', 'exec'))
    return _ev['r']
